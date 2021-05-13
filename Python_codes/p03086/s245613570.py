import sys
S = input()
maxer = 0
count = 0
for i in range( len(S) ):
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        count += 1
        if maxer < count:
            maxer = count
    else:
        count = 0
print( maxer )