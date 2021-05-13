S = input()
s_list = [i for i in S]


eng_list = ['a','b','c','d','e'
    , 'f', 'g', 'h','i','j'
    , 'k', 'l', 'm','n','o'
    , 'p', 'q', 'r','s','t'
    , 'u', 'v', 'w','x','y','z']

dif = set(eng_list) - set(s_list)
if list(dif) == []:
    print('None')
else:print(sorted(list(dif))[0])
