# 754
S =input()
m = 753 
for i in range(len(S)-2):
    tmp=(S[i:i+3])
    m=min(abs(753-int(tmp)),m)
print(m)