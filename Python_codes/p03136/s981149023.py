N=int(input())
input_list=list(map(int,input().split(" ")))

max_input=max(input_list)
Sum_input=sum(input_list)-max_input
if max_input<Sum_input:
    print("Yes")
else:
    print("No")