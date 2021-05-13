import re
print("Yes" if re.search(r".*?C.*?F.*?", input()) else "No")