N = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

num = len(a)//3
ans = sum([a[2*x+1] for x in range(num)])
print(ans)



