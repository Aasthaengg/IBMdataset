N = int(input())
dictionary = dict(AC=0, WA=0, TLE=0, RE=0)
for _ in range(N):
    s = input()
    dictionary[s] += 1

for key in dictionary.keys():
    print('%s x %d'%(key, dictionary[key]))