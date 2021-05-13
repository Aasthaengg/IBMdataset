s = str(input())
start = 0
end = 0
#for i in range(len(s)):
#    if s[i]=='A' and start==0:
#        start = i
#    if s[-(i+1)]=='Z' and end==0:
#        end = len(s)-i
#    if start != 0 and end != 0:
#        break
for i in range(len(s)):
    if s[i]=='A':
        start = i
        break
for i in range(len(s)):
    if s[i]=='Z':
        end = i
print(end-start+1)