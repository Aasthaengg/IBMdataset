N = int(input())
a = list(map(int,input().split()))

mean = sum(a) / N

a_dif = [(i, abs(v-mean)) for i,v in enumerate(a)]

a_dif = sorted(a_dif, key=lambda x:x[1])
print(a_dif[0][0])
