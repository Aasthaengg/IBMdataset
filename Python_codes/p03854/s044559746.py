import re
                                      
S = input()
S = re.sub("eraser", "", S)
S = re.sub("erase", "", S)
S = re.sub("dreamer", "", S)
S = re.sub("dream", "", S)
print("YES" if len(S) == 0 else "NO")