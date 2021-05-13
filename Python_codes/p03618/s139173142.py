a=raw_input()
cnt=[0]*26
for ch in a:
	cnt[ord(ch)-ord('a')]+=1
result=1+len(a)*(len(a)-1)/2
for i in range(26):
	result-=cnt[i]*(cnt[i]-1)/2
print result