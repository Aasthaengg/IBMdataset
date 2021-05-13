import string

S = input()
dictt = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
         'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
dic2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

base = '0'
if len(S) < 26:
    for i in range(len(S)):
        bag = set()
        for s in S[:len(S)-i]:
            bag.add(dictt[s])
        for j in range(1, 27):
            if not j in bag:
                print(S+dic2[j-1])
                exit()
else:
    for i in range(len(S)):
        bag = set()
        for s in S[:len(S)-i]:
            bag.add(dictt[s])
        the_last_letter = (S[len(S)-i-1])
        avail_index = dictt[the_last_letter]
        for j in range(avail_index+1, 27):
            if not j in bag:
                print(S[:len(S)-i-1]+dic2[j-1])
                exit()
    print(-1)
