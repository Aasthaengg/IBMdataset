loop = [int(input())-1]
print("".join(reversed([ chr(ord("a") + code) for code in [ i % 26 for i in loop if loop[-1] // 26  > 0 and (loop.append(loop[-1] // 26 - 1)) or True]])))