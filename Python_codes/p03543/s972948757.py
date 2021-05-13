N = input()
a = "No"

for i in range(2):
    if N[i] == N[i+1] == N[i+2]:
        a = "Yes"
print(a)