N = input()
ans = int(N[0])+9*(len(N)-1)
if not all([N[i] == '9' for i in range(1,len(N))]):
    ans -= 1
print(ans)