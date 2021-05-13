s = input()

str_list = ["dream","dreamer","erase","eraser"]

def checklast(s):
    # print(s)
    for word in str_list:
        if s[-len(word):] == word:
            return s[:-len(word)]
    else:
            return None
    
for i in range(100000):
    if s is None:
        print("NO")
        break
    if len(s) == 0:
        print("YES")
        break
    s = checklast(s)



