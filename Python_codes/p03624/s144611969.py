s=input()
count=0
for i in range(97,97+26):
    if chr(i) not in s:
        print(chr(i))
        count+=1
        break
    
if count==0:
    print("None")