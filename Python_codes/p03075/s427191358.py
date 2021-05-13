l = [int(input()) for i in range(5)]
k = int(input())
p = True

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[j] - l[i] > k:
            p = False
            break          
if p :
    print("Yay!")
else:
    print(":(")