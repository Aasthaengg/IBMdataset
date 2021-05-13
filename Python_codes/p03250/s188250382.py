ABC=[x for x in input().rstrip().split()]
ABC.sort(reverse=True)
ab=ABC[0]+ABC[1]
c=ABC[2]
print(int(ab)+int(c))