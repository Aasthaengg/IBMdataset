S_str = input()
Slen = len(S_str)
S = int(S_str)

S_3 = []
for i in range(2,Slen):
    S_3.append(abs(S//(10**(Slen-i-1))-753))
    S = S % (int(S_str[i-2])*(10**(Slen-i+1)))

print(min(S_3))
