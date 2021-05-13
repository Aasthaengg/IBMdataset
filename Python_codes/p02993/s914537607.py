S = input()
ans = 0
i = 0
while i < 3:
    if S[i] == S[i+1]:
        print("Bad")
        ans += 1
        break
    i += 1
        
if ans == 0:
    print("Good")