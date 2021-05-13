S = input()
mod = 10**9 + 7
dic = {'': 1, 'A': 0, 'B': 0, 'C': 0}
for s in S:
    if s == 'A':
        dic[s] += dic['']

    elif s == 'B':
        dic[s] += dic['A']

    elif s == 'C':
        dic[s] += dic['B']

    elif s == '?':
        dic['C'] = dic['C'] * 3 + dic['B']
        dic['B'] = dic['B'] * 3 + dic['A']
        dic['A'] = dic['A'] * 3 + dic['']
        dic[''] *= 3

    dic[''] %= mod
    dic['A'] %= mod
    dic['B'] %= mod
    dic['C'] %= mod

print(dic['C']%mod)
