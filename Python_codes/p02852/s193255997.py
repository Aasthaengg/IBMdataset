n,m = map(int,input().split())
s = input()

now = n
ans_rev = []
while(now != 0):
    for i in range( max(0,now-m),now+1):
        if(i == now):
            print(-1)
            exit()
        if(s[i] == '1'):
            continue

        ans_rev.append(now - i)
        now = i
        break

print(' '.join(map(str, ans_rev[::-1])))