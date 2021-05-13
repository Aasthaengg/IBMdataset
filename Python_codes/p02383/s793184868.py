sur={1:0,2:0,3:0,4:0,5:0,6:0}
inputs=input().split()
for i in range(6):
    sur[i+1]=int(inputs[i])
dir_of_roll=input()
for i in range(len(dir_of_roll)):
    copy_sur=sur.copy()
    if dir_of_roll[i]=='N':
        sur[1]=copy_sur[2]
        sur[2]=copy_sur[6]
        sur[6]=copy_sur[5]
        sur[5]=copy_sur[1]
    elif dir_of_roll[i]=='S':
        sur[1]=copy_sur[5]
        sur[5]=copy_sur[6]
        sur[6]=copy_sur[2]
        sur[2]=copy_sur[1]
    elif dir_of_roll[i]=='W':
        sur[1]=copy_sur[3]
        sur[3]=copy_sur[6]
        sur[6]=copy_sur[4]
        sur[4]=copy_sur[1]
    elif dir_of_roll[i]=='E':
        sur[1]=copy_sur[4]
        sur[4]=copy_sur[6]
        sur[6]=copy_sur[3]
        sur[3]=copy_sur[1]

print(sur[1])