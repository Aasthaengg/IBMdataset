S = input()
T = input()

ans = "No"

if "".join(sorted(S)) < "".join(sorted(T, reverse=True)):
    ans = "Yes"
    
print(ans)