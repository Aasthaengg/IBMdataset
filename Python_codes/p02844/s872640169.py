n = int(input())
s = input()
l = [0,1,2,3,4,5,6,7,8,9]
ans = 0
for i in l:
    for j in l:
        for k in l:
            a,b,c = i,j,k
            # print(a,b,c)
            for m in s:
                # print(m)
                if a==int(m):
                    # print(i)
                    a = -1
                elif a==-1 and b==int(m):
                    b = -1
                elif b==-1 and c==int(m):
                    ans+=1
                    # print(i,j,k)
                    break
print(ans)