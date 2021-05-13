N = int(input())
length = list(map(int,input().split()))
length.sort(reverse=True)
length_max=length[0]
length_others=sum(length[1:])
if length_others>length_max:
    print("Yes")
else:
    print("No")