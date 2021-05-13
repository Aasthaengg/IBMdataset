S = str(input())

judge = "Good"
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        judge = "Bad"
        break

if judge == "Bad":
    print("Bad")
else:
    print("Good")