from operator import itemgetter
n, *AB = map(int, open(0).read().split())
AB = sorted(zip(AB[::2], AB[1::2]), key=sum, reverse=1)
print(sum(map(itemgetter(0), AB[::2])) - sum(map(itemgetter(1), AB[1::2])))