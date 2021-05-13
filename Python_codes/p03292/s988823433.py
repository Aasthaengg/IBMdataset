a,b,c = map(int, input().split())
ans1 = abs(a-b)+abs(b-c)
ans2 = abs(b-c)+abs(c-a)
ans3 = abs(c-a)+abs(a-b)

print(min(ans1, ans2, ans3))