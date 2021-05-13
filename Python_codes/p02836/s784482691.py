S = input()
 
count = 0
 
for i in range(len(S)//2):
    if not S[i] == S[-(i+1)]:
        count += 1
 
print(count)
