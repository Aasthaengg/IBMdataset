S = str(input())

if all(S[i] != S[i+1] for i in range(3)):
    print("Good")
else:
    print("Bad")
