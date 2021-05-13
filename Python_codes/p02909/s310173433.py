l = ['Sunny','Cloudy','Rainy']
s = input()

save = 0
for i in range(3):
    if(l[i]==s):
        save = i

save = (save+1)%3
print(l[save])