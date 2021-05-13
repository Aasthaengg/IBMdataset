A,B,C=map(int,input().split())
ichi=10*A+B+C
two=A+10*B+C
three=C*10+A+B
print(max(ichi,two,three))
