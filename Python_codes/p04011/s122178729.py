l=[int(input()) for i in range(4)]
print(l[0]*l[2]-max(l[0]-l[1],0)*(l[2]-l[3]))