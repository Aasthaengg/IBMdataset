T = input() + "E"
ans = "S"

for i in range(len(T)-1):
    if T[i] == "?":
        if ans[i] == "P":
            ans += "D"
        else:
            if T[i+1] == "P" or T[i+1] == "E":
                ans += "D"
            else:
                ans += "P"
    else:
        ans += T[i]        
    
print(ans[1:])