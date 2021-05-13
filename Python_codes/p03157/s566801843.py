h,w=map(int,input().split())

maze=[list(input()) for _ in range(h)]

group=[[0]*w for _ in range(h)]

group_no=0
color_cnt=[]

for y in range(h):
    for x in range(w):
        if group[y][x]==0:
            stack=[(y,x)]
            group_no+=1

            color_cnt_tmp=[0,0]

            while len(stack)>0:
                tmp=stack.pop()
                group[tmp[0]][tmp[1]]=group_no
                #print(tmp)
                if maze[tmp[0]][tmp[1]]=="#":
                    color_cnt_tmp[0]+=1
                else:
                    color_cnt_tmp[1]+=1

                for (ny,nx) in [(0,1),(1,0),(-1,0),(0,-1)]:
                    my=ny+tmp[0]
                    mx=nx+tmp[1]
                    if 0<=my<h and 0<=mx<w:
                        if group[my][mx]==0:
                            if maze[tmp[0]][tmp[1]]!=maze[my][mx]:
                                stack.append((my,mx))
                                group[my][mx]=group_no
            color_cnt.append(color_cnt_tmp)

ans=0
for (b,w) in color_cnt:
    ans+=b*w

print(ans)

