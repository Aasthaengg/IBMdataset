n = int(input())
t, a = map(int, input().split())
h_l = list(map(int, input().split()))

# print(n)
# print(t)
# print(a)
# print(h_l)

min_a_tono_sa = 999999
index = 0
for i in range(len(h_l)):
    h = h_l[i]
    heikin_kion = t - h * 0.006
    # print(heikin_kion)
    a_tono_sa = abs(a - heikin_kion)
    # print(a_tono_sa)
    
    if min_a_tono_sa > a_tono_sa:
        min_a_tono_sa = a_tono_sa
        index = i + 1
        
print(index)