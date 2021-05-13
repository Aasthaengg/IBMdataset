[N, K] = list(map(int, input().split()))
List_l = list(map(int, input().split()))
List_l.sort(reverse = True)
print(sum(List_l[0:K]))