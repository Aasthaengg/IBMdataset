s = input() + "."
comp = []

cur = s[0]
streak = 0
count = 0

for i in range(len(s)):
    if s[i] == cur:
        streak += 1
    else:
        if (len(comp) == 0):
            if cur == ">":
                count += streak*(streak+1)//2
            elif i == (len(s) - 1):
                count += streak*(streak+1)//2
        elif cur == ">":
            prevStreak = comp[-1][1]
            count += (prevStreak*(prevStreak+1) + streak*(streak+1)) // 2
            count -= min(streak, prevStreak)
        elif i == (len(s) - 1):
            if cur == "<":
                count += streak*(streak+1)//2

        comp.append((cur, streak))
        streak = 1
        cur = s[i]

print(count)