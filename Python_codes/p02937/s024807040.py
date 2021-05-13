#O(|S|log|s|)
def main():
	s=input()
	t=input()
	n=len(s)
	now=-1
	ans=1
	if not set(t)<=set(s):#tがsの部分集合でない
		print(-1)
		exit()
	for x in t:
		now=s.find(x,now+1)#nowより大きいところからxを探す
		if now==-1:#nowより大きいところでxが見つからなかったら
			ans+=n
			now=s.find(x)
	print(ans+now)
if __name__ == '__main__':
	main()