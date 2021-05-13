S=list(input())
x='Good'
for i in range(3):
    if S[i]==S[i+1]:
        x='Bad'
        break
print(x)