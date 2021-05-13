a, b = input().split()

if len(set((a,b))) == 1:
    ans = "H"
else:
    ans = "D"
print(ans)