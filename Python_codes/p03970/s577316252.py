# coding: utf-8
# Your code here!

seikai = 'CODEFESTIVAL2016'
matigai_count = 0

s = input()

for i in range(16):
    # print(s[i])
    # print(seikai[i])
    if s[i] == seikai[i]:
        # print('〇')
        pass
    else:
        # print('×')
        matigai_count += 1

print(matigai_count)