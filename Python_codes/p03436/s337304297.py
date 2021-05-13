def conv(S,index,c):
	lstS = list(S)
	lstS[index] = c
	S = ''.join(lstS)

	return S


def DFS(stack,MAP,size,count,goal):
	ret = -1
	newstack = []
	for p in stack:
		if p == goal:
			ret = count
		elif ret == -1:
			y = p[0]
			x = p[1]
			Y = size[0]-1
			X = size[1]-1
			if y != 0:
				if MAP[y-1][x] == '.':
					MAP[y-1] = conv(MAP[y-1],x,'*')
					newstack.append([y-1,x])
			if y != Y:
				if MAP[y+1][x] == '.':
					MAP[y+1] = conv(MAP[y+1],x,'*')
					newstack.append([y+1,x])
			if x != 0:
				if MAP[y][x-1] == '.':
					MAP[y] = conv(MAP[y],x-1,'*')
					newstack.append([y,x-1])
			if x != X:
				if MAP[y][x+1] == '.':
					MAP[y] = conv(MAP[y],x+1,'*')
					newstack.append([y,x+1])
	
	if ret == -1:
		if len(newstack) == 0:
			ret = -1
		else:
			ret = DFS(newstack,MAP,size,count+1,goal)

	return ret


if __name__ == '__main__':
	H, W = map(int, input().split())

	MAP = []
	black = 0

	for y in range(H):
		IN = input() 
		MAP.append(IN)
		black += IN.count('#')

	step = DFS([[0,0]],MAP,[H,W],0,[H-1,W-1])

	if step == -1:
		ans = -1
	else:
		ans = H*W - step - 1 - black

	print(ans)