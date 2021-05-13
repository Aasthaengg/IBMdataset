S = list(input())

if S[0]!="A":
    print("WA")
    exit()

if S[2:len(S)-1].count("C")!=1:
    print("WA")
    exit()

count = 0
for i in range(0,len(S),1):
    if ord(S[i])<95:
        count+=1

if count !=2:
    print("WA")
    exit()

print("AC")