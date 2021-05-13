
N = int(input())
print(0)
s = input()
if s=="Vacant":
    exit()
left=0
right=N
l_state = r_state = s
while True:
    center = (left+right)//2
    print(center)
    s = input()
    if s == "Vacant":
        exit()
    if ((center-left)%2) ^ (s!=l_state):
        right = center
        r_state = s
    else:
        left = center
        l_state = s
