n=int(input())
t,a=[int(i) for i in input().split()]
h_list=[int(i) for i in input().split()]


a_list=[abs(a-(t-i*0.006)) for i in h_list]

print(a_list.index(min(a_list))+1)