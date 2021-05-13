S=input()
judge=0
for i in range(0,3):
    if S[i]==S[i+1]:
        judge+=1
if judge>=1:
    print("Bad")
else:
    print("Good")