from collections import deque
n = int(input())

num_to_alp = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
alp_to_num = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
words = deque([[0]])

def next_letters(x):
    letters = deque([])
    for i in range(x + 2):
        letters.append(i)
    return letters

while len(words[0]) < n:
    word = words.popleft()
    letters = next_letters(max(word))
    for l in letters:
        l = [l]
        words.append(word + l)

for word in words:
    word = [num_to_alp[i] for i in word]
    print(''.join(word))
