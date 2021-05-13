# S = "erasedream"
#
# ARR = ['dream', 'dreamer', 'erase', 'eraser']

# S = "erasedream"
# S = "dreameraser"
# S = "dreamerer"

S = input()
def calculate(s):

    index = 0
    isOK = True
    while index < len(s):

        #p1 = 'dreameraser'
        p1 = s[index:index + 11]
        if p1 == 'dreameraser':
            index += 11
            continue
        #p2 = 'dreamerase'

        p2 = s[index:index + 10]
        if p2 == 'dreamerase':
            index += 10
            continue

        s1 = s[index:index+7]

        if s1 == 'dreamer':
            index += 7
            continue

        s2 = s[index:index+6]

        if s2 == 'eraser':
            index += 6
            continue

        s3 = s[index:index+5]

        if s3 == 'erase':
            index += 5
            continue

        if s3 == 'dream':
            index += 5
            continue

        isOK = False
        break

    if isOK:
        print("YES")
    else:
        print("NO")
calculate(S)