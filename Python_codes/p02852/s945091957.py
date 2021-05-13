n,m = map(int,input().split())
s = str(input())
now = n
ans = ""
while now != 0:
    for num in range(min(m,now),0,-1):
        if s[now-num] == "0":
            now -= num
            ans=str(num)+" "+ans
            break
        else:
            if num == 1:
                print(-1)
                exit()
print(ans)