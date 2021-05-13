n, *a_l = map(int, open(0).read().split())
multi_4 = sum([1 for a in a_l if a%4 == 0])
multi_2 = sum([1 for a in a_l if a%2 == 0]) - multi_4
multi_1 = n - ( multi_2 + multi_4 )
print('Yes' if (multi_2%2 + multi_1) <= multi_4 + 1 else 'No')