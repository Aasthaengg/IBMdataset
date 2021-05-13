a,b,c = raw_input().split()
a,b,c = map(int,(a,b,c))

total=0
for divisor_candidate_num in range(a,b+1):
    if c%divisor_candidate_num==0:
        total +=1
print total